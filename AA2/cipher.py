AllCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()}{\/?'

def cipher(plaintext, n):
    global  AllCharacters
    ciphertext = ''

    # Use 'getKey(n)' method to get the key and save it in 'n'
    n =getKey(n)

    for char in plaintext:
        if char in AllCharacters:
            currentPosition = AllCharacters.find(char)
            ciphertext += AllCharacters[(currentPosition + n ) % 77]
        else:
            ciphertext += char

    return ciphertext
        
def decipher(ciphertext, n):
    global  AllCharacters
    plaintext = ""

    # Use 'getKey(n)' method to get the key and save it in 'n'
    n= getKey(n)

    for char in ciphertext:
        if char in AllCharacters:
            currentPosition = AllCharacters.find(char)
            plaintext += AllCharacters[(currentPosition - n) % 77]       
        else:
            plaintext += char
            
    return(plaintext)

# define getKey(n) function    
def getKey(n):
    # Set the key variable to 0
    key = 0
    # Check if 'n' is a string using isinstance(n, str) 
    if isinstance(n,str):
        # Loop through each 'char' in 'n' 
        for char in n:
           # find ASCII code of "char" using 'ord(char)' and add it to key
           key += ord(char)
    # Else make key equals to n      
    else:
        key = n

    # Return the 'key'
    return key
