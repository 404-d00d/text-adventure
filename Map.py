#FINISHED - DO NOT EDIT

char0 = [1, 2, 4, 1] # [x, y, character determiner, direction(1=N,2=E,3=S,4=W)]

cord = [[0, 0, 1.0], [1, 0, 1.0], [2, 0, 1.0], [3, 0, 1.0], [4, 0, 1.0], #List of coordinates for the map
        [0, 1, 1.0], [1, 1, 3.0], [2, 1, 1.0], [3, 1, 0.0], [4, 1, 2.0],
        [0, 2, 1.0], [1, 2, 0.0], [2, 2, 1.0], [3, 2, 0.0], [4, 2, 1.0],
        [0, 3, 1.0], [1, 3, 0.0], [2, 3, 0.0], [3, 3, 0.0], [4, 3, 1.0],
        [0, 4, 1.0], [1, 4, 5.0], [2, 4, 0.0], [3, 4, 0.0], [4, 4, 1.0],
        [0, 5, 1.0], [1, 5, 1.0], [2, 5, 1.0], [3, 5, 1.0], [4, 5, 1.0]]

charList = [char0] #Meant for multiple characters

act = "" #Used to read string of commands

seconds = 0 #amount of time that passed


def printChar(cordList, n): #Determins what characters should be printed based on third var in array
    if cordList[n][2] == 1:
        return "M"
    elif cordList[n][2] == 2:
        return "N"
    elif cordList[n][2] == 3:
        return "T"
    elif cordList[n][2] == 5:
        return "C"
    else:
        return "."


def replaceChar(cordList, n, charCords): #Determines direction player should face, and corresponding character to be printed
    for x in range(len(charCords)):
        if charCords[x][2] == 4:
            if cordList[n][0] == charCords[x][0] and cordList[n][1] == charCords[x][1]:
                if charCords[x][3] == 1:
                    return "^"
                elif charCords[x][3] == 2:
                    return ">"
                elif charCords[x][3] == 3:
                    return "v"
                elif charCords[x][3] == 4:
                    return "<"
    return printChar(cordList, n)


def displayMap(cordList, y, charCord): #actually displays the map
    x = 1
    while x < len(cordList)+1:
        if x % y == 0:
            if x == 0:
                print(replaceChar(cordList, x-1, charCord), end=" ")
            else:
                print(replaceChar(cordList, x-1, charCord))
        else:
            print(replaceChar(cordList, x-1, charCord), end=" ")
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
    elif (move == "w" and charac[3] == 3) or (move == "d" and charac[3] == 2) or (move == "s" and charac[3] == 1) or (move == "s" and charac[3] == 4):
        x1 = 0
        y1 = 1
        charac[0] += x1
        charac[1] += y1
    elif (move == "w" and charac[3] == 4) or (move == "d" and charac[3] == 3) or (move == "s" and charac[3] == 2) or (move == "s" and charac[3] == 1):
        x1 = -1
        y1 = 0
        charac[0] += x1
        charac[1] += y1
    for z in range(len(obs)):
        if obs[z][0] == charac[0] and obs[z][1] == charac[1]:
            if obs[z][2] > 0:
                charac[0] += (x1*(-1))
                charac[1] += (y1*(-1))
                break


def interact(charac, obj): #governs interaction
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
                ac = input("#: ")
                if ac == "1":
                    if obj[x][2] == 2:
                        obj[x][2] = -2
                        print("You open the door.")
                    elif obj[x][2] == -2:
                        obj[x][2] = 2
                        print("You close the door.")
                elif ac == "2":
                    print("You look at the door.")
                    print("It is not as dusty as the rest of the room, but paint is flaking off.")
                    print("The doorknob is bronze, shiny, and not rusted out.")
                else:
                    print("You decide to do nothing")
            elif obj[x][2] == 3:
                print("You see a toilet.")
                print("It has a lever, and a basin where water is stored.")
                print("1. Interact")
                print("2. Observe")
                ac = input("#: ")
                if ac == "1":
                    print("You push down the lever.")
                    print("*FWOOOOOSH*")
                    print("Water from the bowl flows down into the drain, as water seeps from the sides.")
                    print("The water level goes down, and soon rises back to normal.")
                elif ac == "2":
                    print("You look at the toilet.")
                    print("It looks like a normal household toilet, except caked in grime and looking all rusty.")
                else:
                    print("You decide to do nothing")
            elif obj[x][2] == 5:
                print("You see a bare cot with no sheets.")
                print("It has a pillow on it though.")
                print("1. Interact")
                print("2. Observe")
                ac = input("#: ")
                if ac == "1":
                    print("You decide to lay on the cot.")
                    print("It feels super uncomfortable, so you get up quickly.")
                elif ac == "2":
                    print("You look at the cot.")
                    print("The metal frame is rusted and the bedding itself looks moldy and dusty.")
                else:
                    print("You decide to do nothing")


while act != "08202002": #where the game actually starts
    if char0[0] == 4 and char0[1] == 1:
        break
    else:
        displayMap(cord, 5, charList)
        print("You are in a concrete room.")
        print("There is a toilet in a corner, and a cot across from it.")
        print("Seconds Passed: "+str(seconds))
        act = input("CMD: ")
        for x in range(len(act)):
            if act[x] == "e":
                seconds += 1
                if char0[3] == 4:
                    char0[3] = 1
                else:
                    char0[3] += 1
            elif act[x] == "q":
                seconds += 1
                if char0[3] == 1:
                    char0[3] = 4
                else:
                    char0[3] -= 1
            elif act[x] == "w":
                seconds += 1
                moveChar(char0, "w", cord)
            elif act[x] == "d":
                seconds += 1
                moveChar(char0, "d", cord)
            elif act[x] == "s":
                seconds += 1
                moveChar(char0, "s", cord)
            elif act[x] == "a":
                seconds += 1
                moveChar(char0, "a", cord)
            elif act[x] == "f":
                seconds += 1
                interact(char0, cord)
            elif act[x] == " ":
                seconds += 1
            elif act[x] == "~":
                print("Controls:")
                print("w - move forward")
                print("a - sidestep left")
                print("s - move backward")
                print("d - sidestep right")
                print("q - turn left")
                print("e - turn right")
                print("f - interact")
            else:
                print("Not a valid action")

print("--(                 )--")
print("You leave the room.")
print("Game Finished")
print("TIME USED: "+str(seconds)+" SECONDS")
print("Thank you for playing!")