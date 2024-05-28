#This Is Game Of Rock, Paper And Scissor.

#Import Modules
import random
from time import sleep as sl
import sys

while True:

    #Stat Message
    print("Welcome To Rock, Paper And Scissor Game!\n")

    #Game Input
    User = int(input("Press 1 For Rock, 2 For Paper And 3 For Scissors: "))
    Comp = random.randint(1,3)
    
    #GameLogic Of Selection User
    if User == int(1):
        print("You have Chose: Rock")
    elif User == int(2):
        print("You Have Chose: Paper")
    elif User == int(3):
        print("You Have Chose: Scissors")
    else:
        print("Invalid Input, Try Again")
        sys.exit()
    
    sl(1)
    
    #GameLogic Of Selection Computer
    if Comp == int(1):
        print("Computer has Chose: Rock")
    elif Comp == int(2):
        print("Computer has Chose: Paper")
    elif Comp == int(3):
        print("Computer has Chose: Scissors")
    else:
        print("Invalid Input, Try Again")
        sys.exit()
    
    sl(1)
    
    #Game Login For Result
    
    if User == Comp:
        print("Draw!\n\n")
    elif User == int(1) and Comp == int(2):
        print("Computer Won!\n\n")
    elif User == int(1) and  Comp == int(3):
        print("You Won!\n\n")
    elif User == int(2) and Comp == int(1):
        print("You Won!\n\n")
    elif User == int(2) and Comp == int(3):
        print("Computer Won!\n\n")
    elif User == int(3) and Comp == int(1):
        print("Computer Won!\n\n")
    elif User == int(3) and Comp == int(2):
        print("You Won!\n\n")