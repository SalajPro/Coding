a = input("Enter Your name: ")
b = int(input("Enter Your age: "))

def about():
    while True:
        print("Hey,",a)
        if b <= 12:
            print('You are a kid')
        if b >= 13 and b <=17:
            print('You are a teen')
        if b >=18:
            print("You are an adult")

        print("\n \n")

about()
