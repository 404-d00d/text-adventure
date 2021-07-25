char0 = [1, 1, 4, 1] # [x, y, character determiner, direction(1=N,2=E,3=S,4=W)]


cord = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1],
        [0, 1, 1], [1, 1, 0], [2, 1, 1], [3, 1, 0], [4, 1, 2],
        [0, 2, 1], [1, 2, 0], [2, 2, 1], [3, 2, 0], [4, 2, 1],
        [0, 3, 1], [1, 3, 0], [2, 3, 0], [3, 3, 0], [4, 3, 1],
        [0, 4, 1], [1, 4, 1], [2, 4, 1], [3, 4, 1], [4, 4, 1]]

charList = [char0]

act = ""


def printChar(cordList, n):
    if cordList[n][2] == 1:
        return "M"
    elif cordList[n][2] == 2:
        return "N"
    else:
        return "."


def replaceChar(cordList, n, charCords):
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


def displayMap(cordList, y, charCord):
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


def moveChar(charac, move, obs):
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


while act != "stop":
    displayMap(cord, 5, charList)
    print(charList)
    act = input("CMD: ")
    for x in range(len(act)):
        if act[x] == "e":
            if char0[3] == 4:
                char0[3] = 1
            else:
                char0[3] += 1
        elif act[x] == "q":
            if char0[3] == 1:
                char0[3] = 4
            else:
                char0[3] -= 1
        elif act[x] == "w":
            moveChar(char0, "w", cord)
        elif act[x] == "d":
            moveChar(char0, "d", cord)
        elif act[x] == "s":
            moveChar(char0, "s", cord)
        elif act[x] == "a":
            moveChar(char0, "a", cord)
        else:
            print("Not a valid action")
