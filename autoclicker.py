import pyautogui
from time import sleep as sl

def main():
    a=1
    while True:
        pyautogui.click()
        sl(6)
        print(a)
        a = a+1

if __name__ == "__main__":
    main()
