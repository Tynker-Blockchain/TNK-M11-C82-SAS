# Create a list AllCharacters
AllCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()}{\/?'

def cipher(plaintext, n):
    # Access AllCharacters as global
    global  AllCharacters
    ciphertext = ''

    for char in plaintext:
        # Check if char exits in AllCharacters
        if char in AllCharacters:
            # Find position of char in AllCharacters
            currentPosition = AllCharacters.find(char)
            # Calculate the cipher text as AllCharacters[(currentPosition + n ) % 77]
            ciphertext += AllCharacters[(currentPosition + n ) % 77]
        # Remove rest of the elif's
        else:
            ciphertext += char

    return ciphertext
        
def decipher(ciphertext, n):
    # Access specials as global
    global AllCharacters
    plaintext = ""

    for char in ciphertext:
        # Check if char exits in AllCharacters
        if char in AllCharacters:
            # Find position of char in AllCharacters
            currentPosition = AllCharacters.find(char)
            # Calculate the cipher text as AllCharacters[(currentPosition - n ) % 77]
            plaintext += AllCharacters[(currentPosition - n) % 77]
        # Remove rest of the elif's
        else:
            plaintext += char
            
    return(plaintext)
