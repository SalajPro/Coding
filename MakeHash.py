import hashlib

#Function to hashes
def MD5():
    output = hashlib.md5(inputstring.encode())
    print("Hash of the input string in MD5:")
    print(output.hexdigest())

def MD4():
    output = hashlib.md4(inputstring.encode())
    print("Hash of the input string in MD4:")
    print(output.hexdigest())

def SHA256():
    output = hashlib.sha256(inputstring.encode())
    print("Hash of the input string in SHA256:")
    print(output.hexdigest())

def SHA384():
    output = hashlib.sha384(inputstring.encode())
    print("Hash of the input string in SHA384:")
    print(output.hexdigest())

def SHA512():
    output = hashlib.sha512(inputstring.encode())
    print("Hash of the input string in SHA512:")
    print(output.hexdigest())
    
#Input menu
while True:
    lobby = int(input("Which hash you want to use ? \n 1. MD5 \n 2. MD4 \n 3. SHA256 \n 4. SHA384 \n 5. SHA512 \n Enter the number: "))


    inputstring = input("Enter your string: ")

    if lobby == int(1):
        MD5()
    elif lobby == int(2):
        MD4()
    elif lobby == int(3):
        SHA256()
    elif lobby == int(4):
        SHA384()
    elif lobby == int(5):
        SHA512()
    else:
        print("Enter a valid Input!!\n\n")
