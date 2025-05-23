# MADE BY DAVID TRAN
import math
import os
import platform

char0 = [4, 2, 2, 1, 1]  # [character determiner, x, y, direction(1=N,2=E,3=S,4=W), room]

chars = [char0]

act = ""

res = ""

# Clears terminal window so interface looks clean.
def clearScreen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
