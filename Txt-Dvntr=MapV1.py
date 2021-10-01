#MADE BY DAVID TRAN

char0 = [4, 1, 2, 1, 1] # [character determiner, x, y, direction(1=N,2=E,3=S,4=W), room]

cord = [[[1.0, ""], [1.0, ""], [1.0, ""], [6.0, ""], [1.0, ""]], #List of coordinates for the map
        [[1.0, ""], [3.0, ""], [0.0, ""], [0.0, ""], [2.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [5.0, ""], [0.0, ""], [7.0, ""], [1.0, ""]],
        [[1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""]]]

chars = [char0]

act = ""

def representOb(mapCord, x, y):
    if mapCord[y][x][0]==1:
        return "N"
    elif mapCord[y][x][0]==3:
        return "A"
    elif mapCord[y][x][0]==6:
        return "0"
    elif mapCord[y][x][0]==2:
        return "D"
    elif mapCord[y][x][0]==5:
        return "T"
    elif mapCord[y][x][0]==7:
        return "Q"
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

def moveCharacter(character, z):
    if z == 0:
        if character[3] <= 4:
            character[3] += 1
            if character[3] == 5:
                character[3] = 1
    elif z == 1:
        if character[3] >= 1:
            character[3] -= 1
            if character[3] == 0:
                character[3] = 4
    

while char0[4]!=2:
    printDisplay(chars, cord)
    act = input("COMMAND: ")
    for a in range(len(act)):
        if act[a] == "e":
            moveCharacter(char0, 0)
        elif act[a] == "q":
            moveCharacter(char0, 1)
        else:
            print("ERROR: Not a valid command")
