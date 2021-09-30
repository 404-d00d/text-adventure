#MADE BY DAVID TRAN

char0 = [4, 1, 2, 1] # [character determiner, x, y, direction(1=N,2=E,3=S,4=W)]

cord = [[[1.0, ""], [1.0, ""], [1.0, ""], [6.0, ""], [1.0, ""]], #List of coordinates for the map
        [[1.0, ""], [3.0, ""], [0.0, ""], [0.0, ""], [2.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [5.0, ""], [0.0, ""], [7.0, ""], [1.0, ""]],
        [[1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""]]]

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
    if characters[0]==4:
        if characters[3]==1:
            return "^"
        elif characters[3]==2:
            return ">"
        elif characters[3]==3:
            return "v"
        elif characters[3]==4:
            return "<"

for y in range(len(cord)):
    for x in range(len(cord[0])):
        if x == len(cord[0])-1:
            if char0[1]==x and char0[2]==y:
                print(printChar(char0))
            else:
                print(representOb(cord, x, y))
        else:
            if char0[1] == x and char0[2] == y:
                print(printChar(char0), end=" ")
            else:
                print(representOb(cord, x, y), end=" ")
