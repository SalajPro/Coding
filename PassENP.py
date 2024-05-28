# Define a dictionary to map characters (including special characters) to unique identifiers
char_to_id = {
    'a': 'xy', 'b': '3id', 'c': '4kfi', 'd': 'pow', 'e': 'sqa',
    'f': 'mlf', 'g': '9hj', 'h': 'xue', 'i': 'p90', 'j': 'zqe',
    'k': '5rh', 'l': 'poek', 'm': '21sj', 'n': 'fhe', 'o': '15o',
    'p': 'xt1', 'q': 'wodk', 'r': 'dmr', 's': '19s', 't': '46f',
    'u': '21u', 'v': '2edv', 'w': '23qq', 'x': '19d', 'y': '8hg', 'z': '0wa',
    '0': 'es', '1': 'ed', '2': 'ef', '3': 'eg', '4': 'ejll',
    '5': '1az', '6': '54tr', '7': 'vme', '8': 'kali', '9': 'win',
    '!': '37ed', '@': '38ed', '#': '39ed', '$': '40ed', '%': '41ed', '&': '38d',
    '_': 'vrk', '-': '01sa', '+': 'mblg', '=': '86gg', '?': 'ppfw',
}

# Encryption function
def encrypt_password(password):
    encrypted_password = ""
    for char in password:
        if char.lower() in char_to_id:
            encrypted_password += char_to_id[char.lower()]
    return encrypted_password.rstrip("")

# Test the encryption
password = input("Enter Your Password: ")
encrypted = encrypt_password(password)
print("Original Password:", password)
print("Encrypted Password:", encrypted)
