#MADE BY DAVID TRAN
import math

char0 = [4, 1, 2, 1, 1] # [character determiner, x, y, direction(1=N,2=E,3=S,4=W), room]

cord = [[[1.0, ""], [1.0, ""], [1.0, ""], [6.0, ""], [1.0, ""]], #List of coordinates for the map
        [[1.0, ""], [3.1, ""], [0.0, ""], [0.0, ""], [2.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [5.0, ""], [0.0, ""], [7.0, ""], [1.0, ""]],
        [[1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""]]]

chars = [char0]

act = ""

def representOb(mapCord, x, y):
    if math.floor(mapCord[y][x][0])==1:
        return "N"
    elif math.floor(mapCord[y][x][0])==3:
        return "A"
    elif math.floor(mapCord[y][x][0])==6:
        return "0"
    elif math.floor(mapCord[y][x][0])==2:
        return "|"
    elif math.floor(mapCord[y][x][0])==5:
        return "T"
    elif math.floor(mapCord[y][x][0])==7:
        return "Q"
    elif math.floor(mapCord[y][x][0])==-2:
        return "_"
    else:
        return "."

def printChar(characters):
    for x in range(len(characters)):
        if characters[x][0]==4:
            if characters[x][3]==1:
                return "^"
            elif characters[x][3]==2:
                return ">"
            elif characters[x][3]==3:
                return "v"
            elif characters[x][3]==4:
                return "<"

def printDisplay(characters, mapCord):
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            charac = False
            if x == len(mapCord[0])-1:
                for z in range(len(characters)):
                    if characters[z][1]==x and characters[z][2]==y:
                        print(printChar(characters))
                        charac = True
                if not charac:
                    print(representOb(mapCord, x, y))
            else:
                for z in range(len(characters)):
                    if characters[z][1]==x and characters[z][2]==y:
                        print(printChar(characters), end=" ")
                        charac = True
                if not charac:
                    print(representOb(mapCord, x, y), end=" ")
    print("-----")

def moveCharacter(character, mapCord, z):
    x1 = 0
    y1 = 0
    w = 0
    v = 0
    if z == "e":
        if character[3] <= 4:
            character[3] += 1
            if character[3] == 5:
                character[3] = 1
    elif z == "q":
        if character[3] >= 1:
            character[3] -= 1
            if character[3] == 0:
                character[3] = 4
    elif (z == "w" and character[3] == 1) or (z == "d" and character[3] == 4) or (z == "s" and character[3] == 3) or (z == "a" and character[3] == 2):
        x1 = 0
        y1 = -1
    elif (z == "w" and character[3] == 2) or (z == "d" and character[3] == 1) or (z == "s" and character[3] == 4) or (z == "a" and character[3] == 3):
        x1 = 1
        y1 = 0
    elif (z == "w" and character[3] == 3) or (z == "d" and character[3] == 2) or (z == "s" and character[3] == 1) or (z == "a" and character[3] == 4):
        x1 = 0
        y1 = 1
    elif (z == "w" and character[3] == 4) or (z == "d" and character[3] == 3) or (z == "s" and character[3] == 2) or (z == "a" and character[3] == 1):
        x1 = -1
        y1 = 0
    character[1] += x1
    character[2] += y1
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            if character[1]==x and character[2]==y and mapCord[y][x][0]>0:
                character[1] += (x1*-1)
                character[2] += (y1*-1)
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            if mapCord[y][x][0]<=0:
                w += 1
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            if (character[1]!=x or character[2]!=y) and mapCord[y][x][0]<=0:
                v += 1
    if w == v:
        character[1] += (x1*-1)
        character[2] += (y1*-1)

def interactObj(character, mapCord):
    inp = ""
    x1 = 0
    y1 = 0
    if character[3]==1:
        x1 = 0
        y1 = -1
    elif character[3]==2:
        x1 = 1
        y1 = 0
    elif character[3]==3:
        x1 = 0
        y1 = 1
    elif character[3]==4:
        x1 = -1
        y1 = 0
    for y in range(len(mapCord)):
        for x in range(len(mapCord[0])):
            if character[1]+x1 == x and character[2]+y1 == y:
                if math.floor(mapCord[y][x][0])==3:
                    print("You see a toilet.\n"
                          "It is porcelain white, with no blemishes or marks on the body.\n"
                          "The tank lid and tank of the toilet appear to be bolted to the toilet basin and the wall itself.\n"
                          "The toilet lid and toilet basin are white and clean as the rest of the toilet.\n"
                          "The toilet is shiny, reflecting the light from the celing light tubes.\n"
                          "The toilet lid is closed.")
                    print("1. Look Closer\n"
                          "2. Interact\n"
                          "Any Other Option. Do Nothing")
                    inp = input(": ")
                    if inp == "1":
                        if mapCord[y][x][0] == 3:
                            print("You lift up the toilet lid.\n"
                                  "The bowl is clear and clean.\n"
                                  "The water in the bowl is transparent, letting you see the inside of the toilet bowl.\n"
                                  "Much like the outside of the toilet, the inside of the basin is white.")
                        elif mapCord[y][x][0] == 3.1:
                            print("You lift up the toilet lid.\n"
                                  "The bowl is filled with water, chunks of food, and bile.\n"
                                  "The bile and food chunks float on the water's surface, and are mixed together cleanly.\n"
                                  "It's hard to tell what is bile and what are the food chunks.\n"
                                  "You immediately close the toilet lid, just to avoid adding more to that accursed pile.")
                    elif inp == "2":
                        print("You push down on the toilet handle on the tank.\n"
                              "You hear the sound of water flowing into the toilet bowl, followed by the sound of water rushing down the pipes.\n"
                              "It's eventually followed by the rush of water back into the toilet basin.")
                        mapCord[y][x][0]=3
                    else:
                        print("You do nothing.")
                elif mapCord[y][x][0]==abs(2):
                    print("1. Look Closer\n"
                          "2. Interact\n"
                          "Any Other Option. Do Nothing")
                    inp = input(": ")

def gamePlay(action):
    for a in range(len(act)):
        if act[a] == "e":
            moveCharacter(char0, cord, "e")
        elif act[a] == "q":
            moveCharacter(char0, cord, "q")
        elif act[a] == "w":
            moveCharacter(char0, cord, "w")
        elif act[a] == "s":
            moveCharacter(char0, cord, "s")
        elif act[a] == "a":
            moveCharacter(char0, cord, "a")
        elif act[a] == "d":
            moveCharacter(char0, cord, "d")
        elif act[a] == "f":
            interactObj(char0, cord)
        else:
            print("ERROR: Not a valid command")

            
print("You wake up, and find yourself on the floor, laying on your back.\n"
      "You blink rapidly, and soon push yourself off the ground, and stand upright, your drowsiness fading as quickly as your woke up.")

while char0[4]!=2:
    if char0[1]==4 and char0[2]==1:
        char0[4]=2
    else:
        printDisplay(chars, cord)
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
