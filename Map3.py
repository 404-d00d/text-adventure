char0 = [1, 2, 4, 1] # [x, y, character determiner, direction(1=N,2=E,3=S,4=W)]

cord = [[1.0, 1.0, 1.0, 1.0, 1.0], #List of coordinates for the map
        [1.0, 3.0, 1.0, 0.0, 2.0],
        [1.0, 0.0, 1.0, 0.0, 1.0],
        [1.0, 0.0, 0.0, 0.0, 1.0],
        [1.0, 5.0, 0.0, 0.0, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0]]

cord1 = [[],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         []]

charList = [char0] #Meant for multiple characters

act = "" #Used to read string of commands

seconds = 0 #amount of time that passed

reaction = ""

inCord = 0


def printChar(cordList, x, y): #Determins what characters should be printed based on third var in array
    if cordList[x][y] == 1: #Wall
        return "M"
    elif cordList[x][y] == 2: #Regular door
        return "N"
    elif cordList[x][y] == 3: #Toilet
        return "T"
    elif cordList[x][y] == 5: #Cot
        return "C"
    elif cordList[x][y] == 6: #Keypad door
        return "B"
    elif cordList[x][y] == 7: #Dead body
        return "R"
    elif cordList[x][y] == -4: #Dead body
        return "@"
    else:
        return "."


def replaceChar(cordList, charCords): #Determines direction player should face, and corresponding character to be printed
    for x in range(len(charCords)):
        if charCords[x][2] == 4:
            for y in range(len(cordList)):
                for z in range(len(cordList[0])):
                    if y == charCords[x][0] and z == charCords[x][1]:
                        if charCords[x][3] == 1:
                            return "^"
                        elif charCords[x][3] == 2:
                            return ">"
                        elif charCords[x][3] == 3:
                            return "v"
                        elif charCords[x][3] == 4:
                            return "<"
    return printChar(cordList, y, z)


def displayMap(cordList, y, charCord): #actually displays the map
    x = 1
    while x < len(cordList):
        if x % y == 0:
            if x == 0:
                print(replaceChar(cordList, charCord), end=" ")
            else:
                print(replaceChar(cordList, charCord))
        else:
            print(replaceChar(cordList, charCord), end=" ")
        x += 1
    print("---")


def moveChar(charac, move, obs): #Moves the character
    x1 = 0
    y1 = 0
    if (move == "w" and charac[3] == 1) or (move == "d" and charac[3] == 4) or (move == "s" and charac[3] == 3) or (move == "a" and charac[3] == 2):
        x1 = 0
        y1 = -1
        charac[0] += x1
        charac[1] += y1
    elif (move == "w" and charac[3] == 2) or (move == "d" and charac[3] == 1) or (move == "s" and charac[3] == 4) or (move == "a" and charac[3] == 3):
        x1 = 1
        y1 = 0
        charac[0] += x1
        charac[1] += y1
    elif (move == "w" and charac[3] == 3) or (move == "d" and charac[3] == 2) or (move == "s" and charac[3] == 1) or (move == "a" and charac[3] == 4):
        x1 = 0
        y1 = 1
        charac[0] += x1
        charac[1] += y1
    elif (move == "w" and charac[3] == 4) or (move == "d" and charac[3] == 3) or (move == "s" and charac[3] == 2) or (move == "a" and charac[3] == 1):
        x1 = -1
        y1 = 0
        charac[0] += x1
        charac[1] += y1
    for z in range(len(obs)):
        if obs[z][0] == charac[0] and obs[z][1] == charac[1] and obs[z][2] > 0:
            charac[0] += (x1*(-1))
            charac[1] += (y1*(-1))
            break
    y3 = 0
    for z in range(len(obs)):
        if obs[z][2] <= 0:
            y3 += 1
    y2 = 0
    for z in range(len(obs)):
        if (obs[z][0] != charac[0] or obs[z][1] != charac[1]) and obs[z][2] <= 0:
            y2 += 1
    if y2 == y3:
        charac[0] += (x1 * (-1))
        charac[1] += (y1 * (-1))


def Interact(charac, obj): #governs Interaction
    global reaction
    x1 = 0
    y1 = 0
    if charac[3] == 1:
        y1 = -1
    elif charac[3] == 3:
        y1 = 1
    elif charac[3] == 2:
        x1 = 1
    elif charac[3] == 4:
        x1 = -1
    for x in range(len(obj)):
        if obj[x][0] == charac[0] + x1 and obj[x][1] == charac[1] + y1:
            if abs(obj[x][2]) == 2:
                print("You see a door.")
                print("It is lighter than the rest of the room, but is still gray.")
                print("1. Interact")
                print("2. Observe")
                print("ANY OTHER KEY. Do Nothing")
                ac = input("#: ")
                if ac == "1":
                    if obj[x][2] == 2:
                        obj[x][2] = -2
                        reaction = ("You open the door.")
                    elif obj[x][2] == -2:
                        obj[x][2] = 2
                        reaction = ("You close the door.")
                elif ac == "2":
                    reaction = ("You look at the door.\n"
                                "It is not as dusty as the rest of the room, but paint is flaking off.\n"
                                "The doorknob is bronze, shiny, and not rusted out.")
                else:
                    reaction = ("You decide to do nothing")
            elif obj[x][2] == 3:
                print("You see a toilet.")
                print("It has a lever, and a basin where water is stored.")
                print("1. Interact")
                print("2. Observe")
                print("ANY OTHER KEY. Do Nothing")
                ac = input("#: ")
                if ac == "1":
                    reaction = ("You push down the lever.\n"
                                "*FWOOOOOSH*\n"
                                "Water from the bowl flows down into the drain, as water seeps from the sides.\n"
                                "The water level goes down, and soon rises back to normal.")
                elif ac == "2":
                    reaction = ("You look at the toilet.\n"
                                "It looks like a normal household toilet, except caked in grime and looking all rusty.")
                else:
                    reaction = ("You decide to do nothing.")
            elif obj[x][2] == 5:
                print("You see a bare cot with no sheets.")
                print("It has a pillow on it though.")
                print("1. Interact")
                print("2. Observe")
                print("ANY OTHER KEY. Do Nothing")
                ac = input("#: ")
                if ac == "1":
                    reaction = ("You decide to lay on the cot.\n"
                                "It feels super uncomfortable, so you get up quickly.")
                elif ac == "2":
                    reaction = ("You look at the cot.\n"
                                "The metal frame is rusted and the bedding itself looks moldy and dusty.")
                else:
                    reaction = ("You decide to do nothing")
            elif obj[x][2] == -4:
                print("You see a body.")
                print("It is clothed in an orange jumpsuit, with several holes torn in it, as well as bloodstains surrounding them.")
                print("1. Interact")
                print("2. Observe")
                print("ANY OTHER KEY. Do Nothing")
                ac = input("#: ")
                if ac == "1":
                    reaction = ("You flip over the body.\n"
                                "The same holes present in the back are shown in the front.\n"
                                "The jumpsuit at the front is colored a shade of crimson red.\n"
                                "In the pool of blood is a piece of paper.\n"
                                "Although the paper is red, the black text can be seen, which has the numbers '1 3 9 7' on it.\n"
                                "You decide to put the body back in place, so it looks like it has been undisturbed.")
                elif ac == "2":
                    reaction = ("You get a closer look at the body.\n"
                                "The corpse looks white, both in its skin color and because of the lack of blood inside the body.\n"
                                "The face is intact, but the eyes and mouth are open.\n"
                                "Rigor mortis appears to have set in.")
                else:
                    reaction = ("You decide to do nothing")
            elif abs(obj[x][2]) == 6:
                print("You see a door.")
                print("It is the same color as the room, and has a keypad directly to the left side of the door.")
                print("The door has some dust and discoloration on it.")
                print("1. Interact")
                print("2. Observe")
                print("ANY OTHER KEY. Do Nothing")
                ac = input("#: ")
                if ac == "1":
                    print("You decide to interact with the keypad")
                    if obj[x][2] == 6:
                        print("[1][2][3]")
                        print("[4][5][6]")
                        print("[7][8][9]")
                        print("[ ][0][ ]")
                        act1 = input("#: ")
                        if act1 == "1397":
                            obj[x][2] = -6
                            reaction = ("You press the asterik key to input the code.\n"
                                        "You hear a high pitched beep.\n"
                                        "The door is unlocked.\n"
                                        "It slides open from the top")
                        else:
                            reaction = ("You press the asterik key to input the code.\n"
                                        "You hear a low pitched beep.\n"
                                        "The door stays in its place.")
                    else:
                        reaction = ("The door is already unlocked")
                elif ac == "2":
                    reaction = ("You look at the door.\n"
                                "The keypad looks as clean as the door, and is silver in color, with the shine to match.\n"
                                "It appears that there is wear on the buttons.")
                else:
                    reaction = ("You decide to do nothing")


def charControl(cmds, chara, maps, seconds):
    for x in range(len(cmds)):
        if cmds[x] == "e":
            seconds += 1
            if chara[3] == 4:
                chara[3] = 1
            else:
                chara[3] += 1
        elif cmds[x] == "q":
            seconds += 1
            if chara[3] == 1:
                chara[3] = 4
            else:
                chara[3] -= 1
        elif cmds[x] == "w":
            seconds += 1
            moveChar(chara, "w", maps)
        elif cmds[x] == "d":
            seconds += 1
            moveChar(chara, "d", maps)
        elif cmds[x] == "s":
            seconds += 1
            moveChar(chara, "s", maps)
        elif cmds[x] == "a":
            seconds += 1
            moveChar(chara, "a", maps)
        elif cmds[x] == "f":
            seconds += 1
            Interact(chara, maps)
        elif cmds[x] == " ":
            seconds += 1
        elif cmds[x] == "~":
            print("Controls:")
            print("w - move forward")
            print("a - sidestep left")
            print("s - move backward")
            print("d - sidestep right")
            print("q - turn left")
            print("e - turn right")
            print("f - Interact")
        else:
            print("Not a valid action")
    return seconds


while inCord != 2: #where the game actually starts
    if inCord == 0:
        if char0[0] == 4 and char0[1] == 1:
            inCord = 1
            char0[0] = 1
            char0[1] = 1
        else:
            displayMap(cord, 5, charList)
            print(reaction)
            reaction = ""
            print("-----")
            print("You are in a concrete room.")
            print("The lights are harsh and bright, beaming from incadescent lighting tubes.")
            print("The stench of bleach and stagnant water permeates the entire room.")
            print("There is a toilet in a corner, and a cot across from it.")
            print("There is a door with a doorknob on it.")
            print("Seconds Passed: "+str(seconds))
            act = input("CMD: ")
            seconds = charControl(act, char0, cord, seconds)
    elif inCord == 1:
        if char0[0] == 0 and char0[1] == 1:
            inCord = 0
            char0[0] = 3
            char0[1] = 1
        elif char0[0] == 2 and char0[1] == 9:
            inCord = 2
        else:
            displayMap(cord1, 3, charList)
            print(reaction)
            reaction = ""
            print("-----")
            print("You are in a concrete hallway.")
            print("There is a body laying in the middle of the hallway face down, with a pool of blood around it.")
            print("There are two doors, one with a door knob on it, and one with a keypad.")
            print("Seconds Passed: "+str(seconds))
            act = input("CMD: ")
            seconds = charControl(act, char0, cord1, seconds)

print("--(      G A M E   W O N      )--")
print("You leave the room.")
print("Game Finished")
print("TIME USED: "+str(seconds)+" SECONDS")
print("Thank you for playing!")
