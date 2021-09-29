#MADE BY DAVID TRAN

char0 = [4, 1, 2, 1] # [x, y, character determiner, direction(1=N,2=E,3=S,4=W)]

cord = [[[1.0, ""], [1.0, ""], [1.0, ""], [6.0, ""], [1.0, ""]], #List of coordinates for the map
        [[1.0, ""], [3.0, ""], [0.0, ""], [0.0, ""], [2.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [0.0, ""], [0.0, ""], [0.0, ""], [1.0, ""]],
        [[1.0, ""], [5.0, ""], [0.0, ""], [7.0, ""], [1.0, ""]],
        [[1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""], [1.0, ""]]]

def representOb(mapCord, x, y):
    if mapCord[x][y][0]==1:
        return "N"
    elif mapCord[x][y][0]==3:
        return "A"
    elif mapCord[x][y][0]==6:
        return "0"
    elif mapCord[x][y][0]==2:
        return "D"
    else:
        return "."

def printChar(characters):
    if characters[0]==4:
        if characters[3]==1:
            return "^"
        if characters[3]==2:
            return ">"
        if characters[3]==3:
            return "v"
        if characters[3]==4:
            return "<"

for x in range(len(cord)):
    for y in range(len(cord[0])):
        if y == len(cord[0])-1:
            print(representOb(cord, x, y))
        else:
            print(representOb(cord, x, y), end = " ")
