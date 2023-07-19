capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
specials = '!@#$%^&*()}{\/?'

def cipher(plaintext, n):
    global  capitalLetters, lowerLetters, numbers, specials
    ciphertext = ''

    # Use 'getKey(n)' method to get the key and save it in 'n'
    n =getKey(n)

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            ciphertext += numbers[(currentPosition + n ) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            ciphertext += lowerLetters[(currentPosition + n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            ciphertext += capitalLetters[(currentPosition + n) % 26]
        elif char in specials: 
            currentPosition = specials.find(char)
            ciphertext += specials[(currentPosition + n) % 15]
        else:
            ciphertext += char

    return ciphertext
        
def decipher(ciphertext, n):
    global capitalLetters, lowerLetters, numbers, specials
    plaintext = ""

    # Use 'getKey(n)' method to get the key and save it in 'n'
    n= getKey(n)

    for char in ciphertext:
        if char in numbers:
            currentPosition = numbers.find(char)
            plaintext += numbers[(currentPosition - n) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            plaintext += lowerLetters[(currentPosition - n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            plaintext += capitalLetters[(currentPosition - n) % 26] 
            
        elif char in specials:    
            currentPosition = specials.find(char)
            plaintext += specials[(currentPosition - n) % 15]         
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
