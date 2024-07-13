import hashlib

def custom_hash(data):
    # Convert input data to a string (if it isn't already)
    if not isinstance(data, str):
        data = str(data)
    
    # Initialize a variable to hold the hash value
    hash_value = 0
    
    # Iterate over each character in the data
    for char in data:
        # Update the hash value by adding the ASCII value of the character
        hash_value += ord(char)
        
        # Apply a simple transformation (e.g., bitwise operations)
        hash_value = (hash_value << 5) - hash_value
    
    # Ensure the hash value is within a certain range (e.g., 32-bit integer)
    hash_value = hash_value & 0xFFFFFFFF
    
    return hash_value

def convert_to_md5(hash_value):
    # Convert the hash value to a string and encode it to bytes
    hash_str = str(hash_value).encode('utf-8')
    
    # Create an MD5 hash object and update it with the hash value
    md5_hash = hashlib.md5()
    md5_hash.update(hash_str)
    
    # Return the MD5 hash in hexadecimal format
    return md5_hash.hexdigest()

def convert_to_sha512(md5_hash):
    # Encode the MD5 hash to bytes
    md5_bytes = md5_hash.encode('utf-8')
    
    # Create a SHA-512 hash object and update it with the MD5 hash bytes
    sha512_hash = hashlib.sha512()
    sha512_hash.update(md5_bytes)
    
    # Return the SHA-512 hash in hexadecimal format
    return sha512_hash.hexdigest()

def final_hash(data):
    # Apply the custom hash function
    custom_hash_value = custom_hash(data)
    
    # Convert the custom hash value to an MD5 hash
    md5_hash_value = convert_to_md5(custom_hash_value)
    
    # Convert the MD5 hash to a SHA-512 hash
    sha512_hash_value = convert_to_sha512(md5_hash_value)
    
    return sha512_hash_value

# Your final hash
data = input("Enter your data: ")
hash_result = final_hash(data)
print(f"Final hash value is: {hash_result}")
