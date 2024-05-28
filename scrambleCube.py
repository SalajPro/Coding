from time import sleep as sl
import random

moves = ["R","L","U","D","R'","L'","U'","D'",
         "r","r'","u","u'"]

print("Do these scrambles that will come up\n")

i = 0
sl(2)
while (i <= 15):
    print(random.choice(moves),"")
    i = i + 1
    sl(float(1.5))

    if i == 15:
        print("\nThese are are the moves, Now solve!")
        break