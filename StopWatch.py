#Stop Watch

#Modules
from time import sleep

InputForStart = int(input("Enter '1' to start the stop watch \nEnter '2' to Quit: "))

if InputForStart == 2:
    quit()

if InputForStart == 1:
    i = 0
    while True:
        print(i + 1, "Seconds")
        i = i+1
        sleep(1)